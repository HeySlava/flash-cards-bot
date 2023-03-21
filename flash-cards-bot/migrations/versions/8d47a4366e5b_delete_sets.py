"""delete sets

Revision ID: 8d47a4366e5b
Revises: 97a5b9d6abf0
Create Date: 2023-03-22 00:46:39.618438

"""
from __future__ import annotations

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '8d47a4366e5b'
down_revision = '97a5b9d6abf0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table('sets')
    op.drop_table('_alembic_tmp_sets')


def downgrade() -> None:
    op.create_table(
            '_alembic_tmp_sets',
            sa.Column('name', sa.VARCHAR(), nullable=False),
            sa.Column('cdate', sa.DATETIME(), nullable=False),
            sa.Column('udate', sa.DATETIME(), nullable=False),
            sa.Column('user_id', sa.INTEGER(), nullable=False),
            sa.Column('id', sa.VARCHAR(), nullable=False),
            sa.ForeignKeyConstraint(
                ['user_id'], ['users.id'],
                name='fk_sets_user_id_users'),
            sa.PrimaryKeyConstraint('name', name='pk_sets'),
            sa.UniqueConstraint('name', name='uq_sets_name'),
    )

    op.create_table(
            'sets',
            sa.Column('name', sa.VARCHAR(), nullable=False),
            sa.Column('cdate', sa.DATETIME(), nullable=False),
            sa.Column('udate', sa.DATETIME(), nullable=False),
            sa.Column('user_id', sa.INTEGER(), nullable=False),
            sa.ForeignKeyConstraint(
                ['user_id'], ['users.id'],
                name='fk_sets_user_id_users'),
            sa.PrimaryKeyConstraint('name', name='pk_sets'),
    )
