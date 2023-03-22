"""sets.id as fk for cards

Revision ID: 8236cccbbd7b
Revises: 7d79fd513d58
Create Date: 2023-03-22 01:30:01.122563

"""
from __future__ import annotations

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '8236cccbbd7b'
down_revision = '7d79fd513d58'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.add_column(sa.Column('set_id', sa.String(), nullable=False))
        batch_op.create_foreign_key(
                batch_op.f('fk_cards_set_id_sets'), 'sets', ['set_id'], ['id']
            )


def downgrade() -> None:
    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_cards_set_id_sets'), type_='foreignkey')
        batch_op.drop_column('set_id')
