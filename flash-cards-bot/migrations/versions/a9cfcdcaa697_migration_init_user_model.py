"""Migration: init user model

Revision ID: a9cfcdcaa697
Revises: a39a4f7c17f8
Create Date: 2023-03-03 11:46:59.486943

"""
from __future__ import annotations

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'a9cfcdcaa697'
down_revision = 'a39a4f7c17f8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
            'users',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('state', sa.Enum('INPUT_SET_NAME', name='states'), nullable=True),
            sa.Column('cdate', sa.DateTime(), nullable=False),
            sa.Column('udate', sa.DateTime(), nullable=False),
            sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
        )


def downgrade() -> None:
    op.drop_table('users')
