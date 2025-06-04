from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.mark.parametrize("book_name, expected", [
        ("Приключения лежачего на диване", True),
        ("", False),
        ("Как писать рабочий код: пособие для нейросетей", False),
    ])
    def test_add_new_book_check_name(self, test_book_collector, book_name, expected):
        test_book_collector.add_new_book(book_name)
        assert (book_name in test_book_collector.get_books_genre()) == expected

    def test_add_existing_book(self, test_book_collector):
        test_book_collector.add_new_book("Приключения лежачего на диване")
        test_book_collector.add_new_book("Приключения лежачего на диване")
        assert len(test_book_collector.get_books_genre()) == 1

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
    ])
    def test_get_book_genre(self, test_book_collector, book, genre):
        test_book_collector.add_new_book("Маша и волшебный крендель")
        test_book_collector.set_book_genre("Маша и волшебный крендель", "Фантастика")
        assert test_book_collector.get_books_genre() is not None

    @pytest.mark.parametrize("book, genre", [
        ("Маша и волшебный крендель", "Фантастика"),
        ("Пропажа второго носка", "Детективы"),
        ("1000 и 1 способ дышать", "Комедии"),
    ])

    def test_get_books_with_specific_genre(self, test_book_collector, book, genre):
        test_book_collector.add_new_book("Маша и волшебный крендель")
        test_book_collector.set_book_genre("Маша и волшебный крендель", "Фантастика")
        test_book_collector.add_new_book("Пропажа второго носка")
        test_book_collector.set_book_genre("Пропажа второго носка", "Детективы")
        test_book_collector.add_new_book("1000 и 1 способ дышать")
        test_book_collector.set_book_genre("1000 и 1 способ дышать", "Комедии")
        books = test_book_collector.get_books_with_specific_genre(genre = "Фантастика")
        assert len(books) == 1

    @pytest.mark.parametrize("book, genre", [
        ("Колобок", "Фантастика"),
        ("Высшая математика", "Ужасы"),
    ])

    def test_get_books_for_children(self, test_book_collector, book, genre):
        test_book_collector.add_new_book("Колобок")
        test_book_collector.set_book_genre("Колобок", "Фантастика")
        test_book_collector.add_new_book("Высшая математика")
        test_book_collector.set_book_genre("Высшая математика", "Ужасы")
        assert test_book_collector.get_books_for_children() == ["Колобок"]

    @pytest.mark.parametrize("book, add_to_favorites, expected", [
        ("Кричащий в поле", True, ["Кричащий в поле"]),
        ("Кричащий в поле", False, []),
    ])
    def test_add_book_in_favorites(self, test_book_collector, book, add_to_favorites, expected):
        test_book_collector.add_new_book("Кричащий в поле")
        if add_to_favorites:
            test_book_collector.add_book_in_favorites("Кричащий в поле")
            test_book_collector.add_book_in_favorites(book)
        else:
            test_book_collector.add_book_in_favorites("Кричащий в поле")
        assert test_book_collector.get_list_of_favorites_books() == ["Кричащий в поле"]

    @pytest.mark.parametrize("book, delete_in_favorites, expected", [
        ("Кричащий в поле", True, ["Кричащий в поле"]),
        ("Сплетни нашего двора", True, ["Кричащий в поле", "Сплетни нашего двора"]),
        ("Кричащий в поле", False, []),
    ])

    def test_delete_book_in_favorites(self, book, delete_in_favorites, expected):
        collector = BooksCollector()
        collector.add_new_book("Кричащий в поле")
        collector.add_new_book("Сплетни нашего двора")
        if delete_in_favorites:
            collector.add_book_in_favorites("Кричащий в поле")
            collector.add_book_in_favorites(book)
        else:
            collector.add_book_in_favorites("Кричащий в поле")
            collector.delete_book_from_favorites("Кричащий в поле")
        assert collector.get_list_of_favorites_books() == expected

    def test_get_list_of_favorites_books(self, test_book_collector):
        test_book_collector.add_new_book("Кричащий в поле")
        test_book_collector.add_new_book("Сплетни нашего двора")
        test_book_collector.add_book_in_favorites("Кричащий в поле")
        test_book_collector.add_book_in_favorites("Сплетни нашего двора")
        assert test_book_collector.get_list_of_favorites_books() == ["Кричащий в поле", "Сплетни нашего двора"]