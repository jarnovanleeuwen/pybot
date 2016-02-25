from core.command import Command
import urllib
import json


class GoogleCommand(Command):

    def reply(self, response):
        query = self.arguments
        encoded_query = urllib.urlencode({'q': query})
        url = ('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' +
               encoded_query)
        search_response = urllib.urlopen(url)
        search_results = search_response.read()
        results = json.loads(search_results)
        data = results['responseData']
        hits = data['results']
        if len(hits) > 0:
            reply = self.dialogs['reply_top'] % (len(hits), query)
            for hit in hits:
                reply += hit['url'] + '\n'
            reply += (self.dialogs['reply_bottom'] % data['cursor']
                      ['moreResultsUrl'])
            response.send_message.text = reply
        else:
            response.send_message.text = self.dialogs['no_results'] % query
        return response
