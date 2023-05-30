"""add PerformanceStat

Revision ID: 104d4a614d95
Revises: b2dc41850120
Create Date: 2023-05-27 02:59:14.032373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '104d4a614d95'
down_revision = 'b2dc41850120'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('performance_stat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recording_timestamp', sa.Integer(), nullable=True),
    sa.Column('event_type', sa.String(), nullable=True),
    sa.Column('start_time', sa.Integer(), nullable=True),
    sa.Column('end_time', sa.Integer(), nullable=True),
    sa.Column('window_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_performance_stat'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('performance_stat')
    # ### end Alembic commands ###
