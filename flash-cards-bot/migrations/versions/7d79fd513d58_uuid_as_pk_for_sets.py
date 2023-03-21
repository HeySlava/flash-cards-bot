"""uuid as pk for sets

Revision ID: 7d79fd513d58
Revises: 8d47a4366e5b
Create Date: 2023-03-22 00:48:40.058683

"""
from __future__ import annotations

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '7d79fd513d58'
down_revision = '8d47a4366e5b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
            'sets',
            sa.Column('id', sa.String(), nullable=False),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('cdate', sa.DateTime(), nullable=False),
            sa.Column('udate', sa.DateTime(), nullable=False),
            sa.Column('user_id', sa.Integer(), nullable=False),
            sa.ForeignKeyConstraint(
                ['user_id'], ['users.id'],
                name=op.f('fk_sets_user_id_users')
            ),
            sa.PrimaryKeyConstraint('id', name=op.f('pk_sets')),
            sa.UniqueConstraint('name', name=op.f('uq_sets_name'))
    )


def downgrade() -> None:
    op.drop_table('sets')
