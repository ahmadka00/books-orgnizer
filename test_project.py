from project import add_book, delete_book, book_search



def test_add_book():
    assert add_book("Test Book", "Test Author", "Test Category", "2022-01-01") == "Book added successfully"
    
def test_delete_book():
    assert delete_book("Test Book") == "Book deleted successfully"
    
def test_book_search():
    assert book_search("Test Book") == [(1, "Test Book", "Test Author", "Test Category", "2022-01-01")]
