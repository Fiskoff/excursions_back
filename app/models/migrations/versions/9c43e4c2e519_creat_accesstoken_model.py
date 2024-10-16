"""creat AccessToken model

Revision ID: 9c43e4c2e519
Revises: 41e24d8b73c3
Create Date: 2024-10-14 13:44:52.252989

"""
from typing import Sequence, Union

import fastapi_users_db_sqlalchemy
from alembic import op
import sqlalchemy as sa


revision: str = '9c43e4c2e519'
down_revision: Union[str, None] = '41e24d8b73c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('access_token',
        sa.Column('token', sa.String(length=43), nullable=False),
        sa.Column(
            'created_at',
            fastapi_users_db_sqlalchemy.generics.TIMESTAMPAware(timezone=True),
            nullable=False
        ),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['user.id'],
            name=op.f("fk_access_tokens_user_id_user"),
            ondelete='cascade'
        ),
        sa.PrimaryKeyConstraint('token', name=op.f("pk_access_tokens")),
    )
    op.create_index(
        op.f('ix_access_token_created_at'),
        'access_token',
        ['created_at'],
        unique=False
    )


def downgrade() -> None:
    op.drop_index(op.f('ix_access_token_created_at'), table_name='access_token')
    op.drop_table('access_token')
