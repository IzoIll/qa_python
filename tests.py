from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.mark.parametrize("book_name, expected", [
        ("Приключения лежачего на диване", True),
        ("", False),
        ("Как писать рабочий код: пособие для нейросетей", False),
    ])
    def test_add_new_book_check_name(self, book_name, expected):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected

    def test_add_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Приключения лежачего на диване")
        collector.add_new_book("Приключения лежачего на диване")
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("book, genre, expected_genre", [
        ("Инструкция для воды", "Ужасы", "Ужасы"),
        ("Инструкция для воды", "Манга", ""),
    ])
    def test_set_book_genre(self, book, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == expected_genre

    @pytest.mark.parametrize("book, genre", [
        ("Маша и волшебный крендель", "Фантастика"),
        ("1000 и 1 способ дышать", ""),
    ])
    def test_get_book_genre(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        if genre:
            collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Маша и волшебный крендель")
        collector.set_book_genre("Маша и волшебный крендель", "Фантастика")
        collector.add_new_book("1000 и 1 способ дышать")
        collector.set_book_genre("1000 и 1 способ дышать", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Маша и волшебный крендель", "1000 и 1 способ дышать"]

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Прогулка по вольеру")
        collector.set_book_genre("Прогулка по вольеру", "Комедии")
        assert collector.get_books_genre() == {"Прогулка по вольеру": "Комедии"}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Колобок")
        collector.set_book_genre("Колобок", "Фантастика")
        collector.add_new_book("Высшая математика")
        collector.set_book_genre("Высшая математика", "Ужасы")
        assert collector.get_books_for_children() == ["Колобок"]

    @pytest.mark.parametrize("book, add_to_favorites, expected", [
        ("Кричащий в поле", True, ["Кричащий в поле"]),
        ("Сплетни нашего двора", True, ["Кричащий в поле", "Сплетни нашего двора"]),
        ("Кричащий в поле", False, []),
    ])
    def test_manage_favorites(self, book, add_to_favorites, expected):
        collector = BooksCollector()
        collector.add_new_book("Кричащий в поле")
        collector.add_new_book("Сплетни нашего двора")
        if add_to_favorites:
            collector.add_book_in_favorites("Кричащий в поле")
            collector.add_book_in_favorites(book)
        else:
            collector.add_book_in_favorites("Кричащий в поле")
            collector.delete_book_from_favorites("Кричащий в поле")
        assert collector.get_list_of_favorites_books() == expected

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Кричащий в поле")
        collector.add_new_book("Сплетни нашего двора")
        collector.add_book_in_favorites("Кричащий в поле")
        collector.add_book_in_favorites("Сплетни нашего двора")
        assert collector.get_list_of_favorites_books() == ["Кричащий в поле", "Сплетни нашего двора"]