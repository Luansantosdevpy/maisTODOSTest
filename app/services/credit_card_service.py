from flask import jsonify

from app import app
from app.repositories.credit_card_repository import CreditCardRepository
from app.validation import CreditCardValidator
from app.handlers import CreditCardHandler

credit_card_handler = CreditCardHandler()


class CreditCardService:
    def __init__(self, repository: CreditCardRepository):
        self.repository = repository
        self.validator = CreditCardValidator()

    def list_credit_cards(self):
        app.logger.info('CreditCardService - listCreditCards - call repository to return all credit cards')
        credit_cards = self.repository.list_credit_cards()

        if credit_cards is not None:
            app.logger.info('CreditCardService - listCreditCards - return all credit cards')
            return credit_cards
        else:
            app.logger.error('CreditCardService - listCreditCards - error listing credit cards')
            return None

    def get_credit_card(self, card_id):
        app.logger.info(f'CreditCardService - listCreditCard - call repository to return credit card by ID: {card_id}')
        credit_card = self.repository.get_credit_card(card_id)

        if credit_card:
            app.logger.info(f'CreditCardService - listCreditCard - return credit card by ID: {card_id}')
            return credit_card
        else:
            app.logger.error('CreditCardService - listCreditCard - credit card not found')
            return None

    def create_credit_card(self, payload):
        is_valid_exp_date = self.validator.is_valid_exp_date(payload["exp_date"])
        if is_valid_exp_date is False:
            return {"error": "expiration date is invalid"}

        formatted_exp_date = self.validator.format_exp_date(payload["exp_date"])

        if not formatted_exp_date:
            return {"error": "Invalid expiration date format"}

        validate_card = self.validator.is_valid_card_number(payload["number"])

        if not validate_card:
            app.logger.error('CreditCardService - createCreditCard - card number is invalid')
            return {"error": "Credit card is invalid"}

        brand = self.validator.get_brand_by_card_number(payload["number"])

        app.logger.info('CreditCardService - createCreditCard - encrypt card number')
        credit_card = credit_card_handler.encrypt_credit_card_number(payload["number"])

        new_credit_card = {
            "exp_date": formatted_exp_date,
            "holder": payload["holder"],
            "number": credit_card,
            "cvv": payload["cvv"],
            "brand": brand
        }

        app.logger.info('CreditCardService - createCreditCard - call repository method to create credit card')
        created_credit_card = self.repository.create_credit_card(new_credit_card)

        if created_credit_card:
            app.logger.info('CreditCardService - createCreditCard - credit card created successfully')
            return created_credit_card
        else:
            app.logger.error('CreditCardService - createCreditCard - failed to create')
            return None

    def update_credit_card(self, card_id, payload):
        existing_credit_card = self.repository.get_credit_card(card_id)
        if not existing_credit_card:
            app.logger.error('CreditCardService - updateCreditCard - credit card not found')
            return False

        formatted_exp_date = self.validator.format_exp_date(payload["exp_date"])

        if not formatted_exp_date:
            return False

        validate_card = self.validator.is_valid_card_number(payload["number"])

        if not validate_card:
            app.logger.error('CreditCardService - updateCreditCard - card number is invalid')
            return False

        brand = self.validator.get_brand_by_card_number(payload["number"])

        app.logger.info('CreditCardService - createCreditCard - encrypt card number')
        credit_card = credit_card_handler.encrypt_credit_card_number(payload["number"])

        updated_credit_card = {
            "exp_date": formatted_exp_date,
            "holder": payload["holder"],
            "number": credit_card,
            "cvv": payload["cvv"],
            "brand": brand
        }

        app.logger.info('CreditCardService - updateCreditCard - call repository method to update credit card')
        if self.repository.update_credit_card(card_id, updated_credit_card):
            app.logger.info('CreditCardService - updateCreditCard - credit card updated successfully')
            return True
        else:
            app.logger.error('CreditCardService - updateCreditCard - failed to update')
            return False

    def delete_credit_card(self, card_id):
        existing_credit_card = self.repository.get_credit_card(card_id)
        if not existing_credit_card:
            app.logger.error('CreditCardService - deleteCreditCard - credit card not found')
            return False

        app.logger.info('CreditCardService - deleteCreditCard - call repository method to delete credit card')
        if self.repository.delete_credit_card(card_id):
            app.logger.info('CreditCardService - deleteCreditCard - credit card deleted successfully')
            return True
        else:
            app.logger.error('CreditCardService - deleteCreditCard - failed to delete')
            return False