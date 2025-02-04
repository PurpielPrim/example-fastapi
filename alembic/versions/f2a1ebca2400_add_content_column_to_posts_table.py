"""add content column to posts table

Revision ID: f2a1ebca2400
Revises: c9e14d334ea5
Create Date: 2025-02-04 20:01:46.062642

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2a1ebca2400'
down_revision: Union[str, None] = 'c9e14d334ea5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
