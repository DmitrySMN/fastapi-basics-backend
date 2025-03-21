from core import Base
from datetime import datetime, timezone
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY, INTEGER


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=str(datetime.now(tz=timezone.utc)), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        server_default=str(datetime.now(tz=timezone.utc)), server_onupdate=str(datetime.now(tz=timezone.utc)), onupdate=str(datetime.now(tz=timezone.utc)), nullable=True
    )

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    photo_url: Mapped[str] = mapped_column(nullable=False)
    quantity_in_stock: Mapped[int] = mapped_column(nullable=False)

class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    product_ids: Mapped[list[int]] = mapped_column(ARRAY(INTEGER), nullable=False)
    order_date: Mapped[datetime] = mapped_column(server_default=str(datetime.now(tz=timezone.utc)), nullable=False)
    total_price: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(default="Новый", nullable=False)
    shipping_address: Mapped[str] = mapped_column(nullable=False)