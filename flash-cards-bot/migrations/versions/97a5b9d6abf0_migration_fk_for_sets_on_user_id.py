"""Migration: fk for sets on user(id)

Revision ID: 97a5b9d6abf0
Revises: a9cfcdcaa697
Create Date: 2023-03-03 12:39:13.031222

"""
from __future__ import annotations

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '97a5b9d6abf0'
down_revision = 'a9cfcdcaa697'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('sets', schema=None) as batch_op:
        batch_op.add_column(
                sa.Column('user_id', sa.Integer(), nullable=False),
            )
        batch_op.create_foreign_key(
                batch_op.f('fk_sets_user_id_users'),
                'users', ['user_id'], ['id'],
            )


def downgrade() -> None:
    with op.batch_alter_table('sets', schema=None) as batch_op:
        batch_op.drop_constraint(
                batch_op.f('fk_sets_user_id_users'),
                type_='foreignkey',
            )
        batch_op.drop_column('user_id')
