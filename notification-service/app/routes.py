from fastapi import APIRouter

from .schemas import (
    OrderConfirmation,
    PaymentConfirmation,
    ShipmentNotification
)


router = APIRouter(
    prefix="/notification",
    tags=["Notifications"]
)


@router.post("/order-confirmation")
def send_order_confirmation(notification: OrderConfirmation):

    message = (
        f"Order confirmation notification sent to "
        f"{notification.customer_email} "
        f"for Order ID: {notification.order_id}"
    )

    print(message)

    return {
        "success": True,
        "message": message
    }


@router.post("/payment-confirmation")
def send_payment_confirmation(notification: PaymentConfirmation):

    message = (
        f"Payment confirmation sent to "
        f"{notification.customer_email} "
        f"for Payment ID: {notification.payment_id}"
    )

    print(message)

    return {
        "success": True,
        "message": message,
        "amount": notification.amount
    }


@router.post("/shipment")
def send_shipment_notification(notification: ShipmentNotification):

    message = (
        f"Shipment notification sent to "
        f"{notification.customer_email}. "
        f"Tracking Number: {notification.tracking_number}"
    )

    print(message)

    return {
        "success": True,
        "message": message
    }