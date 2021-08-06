from django.test import TestCase
from library.models import Book, Reader,Borrowing
# from django.core.urlresovers import reverse


class BookMethodTests(TestCase):
    def test_ensure_quantity_are_positive(self):
        cat = Book(ISBN="9787532725694", title="This is the string I insert ", author="haimingwei", press="Shanghai",
                   description="Just hope to walk in", category="novel", price="5.00", cover="9787544242516.jpg",
                   location="thth", quantity=10)
        cat = Book()
        cat.save()
        self.assertEqual((cat.quantity >= 0), True)

class ViewTest(TestCase):
    def test_view(self):
        book =Book.objects.create(ISBN="9787532725694", title="This is the string I insert ", author="haimingwei", press="shanghai",
                   description="Just hope to walk in", category="novel", price="5.00", cover="9787544242516.jpg",
                   location="thth", quantity=10)
        response = self.client.get('/search/?keyword=_Booklist')
        self.assertEqual(response.status_code,200)

class ReaderTestCase(TestCase):

    def test_models(self):
        # add a user object
        dog = Reader(user_id=6, phone=1234587359, name="hi")
        dog.save()
        self.assertEqual((dog.max_borrowing <= 5), True)


class BorrowingTests(TestCase):
    def test_borrowing(self):
        tree = Borrowing(reader_id=6,ISBN_id="123456789098",date_issued="2020-3-12",date_due_to_returned="2020-4-12")
        tree.save()
        self.assertEqual((tree.amount_of_fine >= 0), True)




'''
class ReaderTestCase(TestCase):

    def test_models(self):
        # add a user object
        dog = Reader(user_id=6,phone=1234587359,name="hi")
        dog.save()
        self.assertEqual(Reader.objects.filter(id=56).count(),1,'没有插入成功')




'''
