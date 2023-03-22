"""Added column current_set for user

Revision ID: fc89135d446e
Revises: 8236cccbbd7b
Create Date: 2023-03-22 18:59:45.454473

"""
from __future__ import annotations

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'fc89135d446e'
down_revision = '8236cccbbd7b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('current_set', sa.String(), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('current_set')
