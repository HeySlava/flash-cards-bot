"""Create sets and cards

Revision ID: a39a4f7c17f8
Revises:
Create Date: 2023-03-03 10:44:24.892555

"""
from __future__ import annotations

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'a39a4f7c17f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
            'cards',
            sa.Column('term', sa.String(), nullable=False),
            sa.Column('definition', sa.String(), nullable=True),
            sa.Column('cdate', sa.DateTime(), nullable=False),
            sa.Column('udate', sa.DateTime(), nullable=False),
            sa.PrimaryKeyConstraint('term', name=op.f('pk_cards')),
        )
    op.create_table(
            'sets',
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('cdate', sa.DateTime(), nullable=False),
            sa.Column('udate', sa.DateTime(), nullable=False),
            sa.PrimaryKeyConstraint('name', name=op.f('pk_sets')),
        )


def downgrade() -> None:
    op.drop_table('sets')
    op.drop_table('cards')
