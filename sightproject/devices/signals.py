from django.db.models.signals import post_save
from django.dispatch import receiver

from devices.models import Switch, SwitchStatus, SwitchTerminal, Terminal, TerminalStatus

@receiver(post_save, sender='core.RawData')
def new_entry_handler(sender, instance, created, **kwargs):
    """
    Handles actions after an instance of RawData is saved.
    """
    
    # Check if a NEW entry was created
    if created:
        print(f"--- New log created! ID: {instance.pk}")

        # Get Switch
        switch = Switch.objects.get(switch_label=instance.switch_label)
        if switch:
            switch_id = switch.switch_id

            terminal_1 = Terminal.objects.get(terminal_code='T1')
            terminal_2 = Terminal.objects.get(terminal_code='T2')
            terminal_3 = Terminal.objects.get(terminal_code='T3')
            terminal_4 = Terminal.objects.get(terminal_code='T4')
            terminal_5 = Terminal.objects.get(terminal_code='T5')

            # Get Switch Terminal Id
            switch_terminal_1 = SwitchTerminal.objects.get(
                switch_id = switch_id, 
                terminal_id = terminal_1.terminal_id
            )

            switch_terminal_2 = SwitchTerminal.objects.get(
                switch_id = switch_id, 
                terminal_id = terminal_2.terminal_id
            )

            switch_terminal_3 = SwitchTerminal.objects.get(
                switch_id = switch_id, 
                terminal_id = terminal_3.terminal_id
            )

            switch_terminal_4 = SwitchTerminal.objects.get(
                switch_id = switch_id, 
                terminal_id = terminal_4.terminal_id
            )

            switch_terminal_5 = SwitchTerminal.objects.get(
                switch_id = switch_id, 
                terminal_id = terminal_5.terminal_id
            )

            if not TerminalStatus.objects.filter(switch_terminal_id=switch_terminal_1.id, log_at= instance.logtime).exists():
                terminal_status_1 = TerminalStatus(switch_terminal_id=switch_terminal_1.id, log_at=instance.logtime, status=instance.t1)
                terminal_status_1.save()

            if not TerminalStatus.objects.filter(switch_terminal_id=switch_terminal_2.id, log_at= instance.logtime).exists():
                terminal_status_2 = TerminalStatus(switch_terminal_id=switch_terminal_2.id, log_at=instance.logtime, status=instance.t2)
                terminal_status_2.save()

            if not TerminalStatus.objects.filter(switch_terminal_id=switch_terminal_3.id, log_at= instance.logtime).exists():
                terminal_status_3 = TerminalStatus(switch_terminal_id=switch_terminal_3.id, log_at=instance.logtime, status=instance.t3)
                terminal_status_3.save()

            if not TerminalStatus.objects.filter(switch_terminal_id=switch_terminal_4.id, log_at= instance.logtime).exists():
                terminal_status_4 = TerminalStatus(switch_terminal_id=switch_terminal_4.id, log_at=instance.logtime, status=instance.t4)
                terminal_status_4.save()

            if not TerminalStatus.objects.filter(switch_terminal_id=switch_terminal_5.id, log_at= instance.logtime).exists():
                terminal_status_5 = TerminalStatus(switch_terminal_id=switch_terminal_5.id, log_at=instance.logtime, status=instance.t5)
                terminal_status_5.save()

            switch_terminal_statuses = [instance.t1, instance.t2, instance.t3, instance.t4, instance.t5];

            switch_status = 0;
            if 1 in switch_terminal_statuses:
                switch_status = 1;
    
            if not SwitchStatus.objects.filter(switch_id=switch_id, log_at= instance.logtime).exists():
                switch_status_entry = SwitchStatus(switch_id=switch_id, log_at=instance.logtime, status=switch_status)
                switch_status_entry.save()

                print(f"--- Switch Status saved for Switch ID: {switch_id} at {instance.logtime} with status {switch_status}")