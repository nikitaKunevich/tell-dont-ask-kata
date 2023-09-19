from dataclasses import dataclass, field

from .order_item import OrderItem
from .order_status import OrderStatus
from use_case.exceptions import OrderCannotBeShippedException, OrderCannotBeShippedTwiceException, \
    ShippedOrdersCannotBeChangedException, RejectedOrderCannotBeApprovedException, \
    ApprovedOrderCannotBeRejectedException


@dataclass
class Order:
    id: int = 0
    total: float = 0
    currency: str = 'EUR'
    items: list[OrderItem] = field(default_factory=list)
    tax: float = 0
    status: OrderStatus = OrderStatus.CREATED

    def ship(self) -> None:
        match self.status:
            case OrderStatus.CREATED | OrderStatus.REJECTED:
                raise OrderCannotBeShippedException()
            case OrderStatus.SHIPPED:
                raise OrderCannotBeShippedTwiceException()
        self.status = OrderStatus.SHIPPED

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)
        self.total += item.taxed_amount
        self.tax += item.tax

    def approve(self) -> None:
        match self.status:
            case OrderStatus.SHIPPED:
                raise ShippedOrdersCannotBeChangedException()
            case OrderStatus.REJECTED:
                raise RejectedOrderCannotBeApprovedException()
        self.status = OrderStatus.APPROVED

    def reject(self) -> None:
        match self.status:
            case OrderStatus.SHIPPED:
                raise ShippedOrdersCannotBeChangedException()
            case OrderStatus.APPROVED:
                raise ApprovedOrderCannotBeRejectedException()
        self.status = OrderStatus.REJECTED
