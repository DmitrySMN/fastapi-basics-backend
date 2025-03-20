from datetime import datetime, timezone
from .core import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=datetime.now(tz=timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        server_default=datetime.now(tz=timezone.utc), server_onupdate=datetime.now(tz=timezone.utc), onupdate=datetime.now(tz=timezone.utc), nullable=True
    )