from core.command import Command
import os


class HelpCommand(Command):

    def reply(self, response):
        if self.arguments == 'help':
            return {'message': self.usage}
        reply = self.dialogs['reply']
        command_list = []
        for name in os.listdir(os.path.dirname(os.path.abspath(__file__))):
            if name.endswith('.py') and name != '__init__.py':
                command_list.append('/' + name[:-3])
        command_list.sort()
        reply += '\n' + '\n'.join(map(str, command_list))
        response.send_message.text = reply
        return response
