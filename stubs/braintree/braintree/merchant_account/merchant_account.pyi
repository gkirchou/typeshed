from _typeshed import Incomplete
from typing import Final

from braintree.configuration import Configuration as Configuration
from braintree.merchant_account import (
    BusinessDetails as BusinessDetails,
    FundingDetails as FundingDetails,
    IndividualDetails as IndividualDetails,
)
from braintree.resource import Resource as Resource

class MerchantAccount(Resource):
    class Status:
        Active: Final = "active"
        Pending: Final = "pending"
        Suspended: Final = "suspended"

    class FundingDestination:
        Bank: Final = "bank"
        Email: Final = "email"
        MobilePhone: Final = "mobile_phone"

    FundingDestinations: type[FundingDestination]
    individual_details: IndividualDetails
    business_details: BusinessDetails
    funding_details: FundingDetails
    master_merchant_account: MerchantAccount
    def __init__(self, gateway, attributes) -> None: ...
    @staticmethod
    def create(params: Incomplete | None = None): ...
    @staticmethod
    def update(id, attributes): ...
    @staticmethod
    def find(id): ...
