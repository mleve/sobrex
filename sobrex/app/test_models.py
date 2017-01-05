from django.test import TestCase
from django.core.exceptions import ValidationError
from app.models import Client, Address

class AddressTestCase(TestCase):

	def test_creation(self):
		addr = Address.objects.create(
			street = "Blanco encalada",
			number = "1771",
			sub_index = "1905",
			city = "Santiago")

		addr.save()

		self.assertEquals(Address.objects.count(),1)

	def test_validation_errors(self):
		addr = Address.objects.create(
			street = "Blanco encalada",
			sub_index = "1905",
			city = "Santiago")
		
		with self.assertRaises(ValidationError):
			addr.full_clean()




