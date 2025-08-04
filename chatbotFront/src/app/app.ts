import { Component, signal } from '@angular/core';
import { ChatComponent } from './chat.component';

@Component({
  selector: 'app-root',
  imports: [ChatComponent],
  template: `
    <h1>TalkJS Chat Application</h1>
    <app-chat></app-chat>
  `,
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('chatbot');
}
