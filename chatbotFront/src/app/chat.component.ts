import { Component } from '@angular/core';
import Talk from 'talkjs';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [],
  template: `
    <div id="talkjs-container" style="height: 600px">Loading chats...</div>
  `,
  styles: '',
})
export class ChatComponent {
  constructor() {
    Talk.ready.then(() => {
      // ✅ Utilisateur humain
      const me = new Talk.User({
        id: 'user_123',
        name: 'Utilisateur',
        email: 'user@example.com',
        photoUrl: 'https://demo.talkjs.com/img/ronald.jpg',
        role: 'default',
      });

      // ✅ Chatbot IA
      const bot = new Talk.User({
        id: 'bot_456',
        name: 'Chatbot IA',
        email: 'bot@example.com',
        photoUrl: 'https://demo.talkjs.com/img/alice.jpg',
        role: 'default',
      });

      const session = new Talk.Session({
        appId: 'tlrnXVFP', // Ton vrai App ID TalkJS
        me: me,
      });

      const conversation = session.getOrCreateConversation('user_123__bot_456'); // ✅ ID fixe qui correspond à l'API
      conversation.setParticipant(me);
      conversation.setParticipant(bot);

      console.log("🔍 Conversation ID utilisé:", 'user_123__bot_456'); // Pour débugger

      const chatbox = session.createChatbox();
      chatbox.select(conversation);
      chatbox.mount(document.getElementById('talkjs-container'));

      // ✅ Quand l'utilisateur envoie un message
      chatbox.on('sendMessage', (event: any) => {
        // ✅ Récupération correcte du message
        const userMessage = event.message.text || event.text || event.message.body;
        console.log("Message envoyé au backend:", userMessage);
        console.log("Event complet:", event); // Pour débugger

        if (!userMessage || userMessage.trim() === '') {
          console.error("Message vide détecté");
          return;
        }

        fetch('http://localhost:5000/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ message: userMessage }),
        })
          .then((res) => res.json())
          .then((data) => {
            console.log("Bot reply reçu du backend :", data.reply);
            // Le message est injecté dans TalkJS automatiquement via le backend
          })
          .catch((err) => {
            console.error('Erreur lors de la communication avec le chatbot :', err);
          });
      });
    });
  }
}
