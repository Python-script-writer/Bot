import telepot
import config

token = config.API_TOKEN
telegramBot = telepot.Bot(token)

def send_message(text):
    telegramBot.sendMessage(text.chat.id, text, parse_mode="Markdown")

class LeadCreationView():
    form_class = LeadForm
    success_url = reverse_lazy('callback')

def form_valid(self, form):
    name = form.cleaned_data['name']
    phone = form.cleaned_data['phone']
    message = "*ЗАЯВКА С САЙТА*:" + "\n" + "*ИМЯ*: " +str(name) + "\n" + "*ТЕЛЕФОН*: " + str(phone)
    send_message(message)
    return super(LeadCreationView, self).form_valid(form)

def form_invalid(self, form):
    return redirect(self.get_success_url())
