from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


class LibraryApp(App):
    def build(self):
        self.library = {}  # Store books as {title: (author, copies)}
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title Label
        self.main_layout.add_widget(Label(text="Library Management System", font_size=24, size_hint=(1, 0.1)))

        # Input Fields
        self.title_input = TextInput(hint_text="Enter Book Title", size_hint=(1, 0.1))
        self.author_input = TextInput(hint_text="Enter Author", size_hint=(1, 0.1))
        self.copies_input = TextInput(hint_text="Enter Number of Copies", size_hint=(1, 0.1), input_filter='int')
        self.main_layout.add_widget(self.title_input)
        self.main_layout.add_widget(self.author_input)
        self.main_layout.add_widget(self.copies_input)

        # Buttons
        add_button = Button(text="Add Book", size_hint=(1, 0.1))
        add_button.bind(on_press=self.add_book)
        self.main_layout.add_widget(add_button)

        view_button = Button(text="View Books", size_hint=(1, 0.1))
        view_button.bind(on_press=self.view_books)
        self.main_layout.add_widget(view_button)

        self.output_label = Label(text="", size_hint=(1, 0.5), valign="top", halign="left")
        self.output_label.bind(size=self.output_label.setter('text_size'))
        scroll_view = ScrollView(size_hint=(1, 0.5))
        scroll_view.add_widget(self.output_label)
        self.main_layout.add_widget(scroll_view)

        return self.main_layout

    def add_book(self, instance):
        title = self.title_input.text.strip()
        author = self.author_input.text.strip()
        copies = self.copies_input.text.strip()

        if title and author and copies:
            copies = int(copies)
            if title in self.library:
                self.library[title] = (author, self.library[title][1] + copies)
                self.output_label.text = f"Added {copies} more copies of '{title}'."
            else:
                self.library[title] = (author, copies)
                self.output_label.text = f"Book '{title}' by {author} added with {copies} copies."
            self.title_input.text = ""
            self.author_input.text = ""
            self.copies_input.text = ""
        else:
            self.output_label.text = "Please fill all fields to add a book."

    def view_books(self, instance):
        if not self.library:
            self.output_label.text = "No books in the library yet."
        else:
            books_list = "Available Books:\n\n"
            for title, (author, copies) in self.library.items():
                books_list += f"Title: {title}, Author: {author}, Copies: {copies}\n"
            self.output_label.text = books_list


if __name__ == "__main__":
    LibraryAp().run()
