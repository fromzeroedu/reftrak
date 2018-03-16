"""empty message

Revision ID: 78817124f4e9
Revises: 
Create Date: 2018-03-16 12:39:18.905428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78817124f4e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('redirect_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=64), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_redirect_list_code'), 'redirect_list', ['code'], unique=False)
    op.create_index(op.f('ix_redirect_list_description'), 'redirect_list', ['description'], unique=False)
    op.create_index(op.f('ix_redirect_list_url'), 'redirect_list', ['url'], unique=False)
    op.create_table('redirect_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=64), nullable=True),
    sa.Column('referrer', sa.String(length=255), nullable=True),
    sa.Column('code', sa.String(length=64), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_redirect_log_code'), 'redirect_log', ['code'], unique=False)
    op.create_index(op.f('ix_redirect_log_ip'), 'redirect_log', ['ip'], unique=False)
    op.create_index(op.f('ix_redirect_log_referrer'), 'redirect_log', ['referrer'], unique=False)
    op.create_index(op.f('ix_redirect_log_timestamp'), 'redirect_log', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_redirect_log_timestamp'), table_name='redirect_log')
    op.drop_index(op.f('ix_redirect_log_referrer'), table_name='redirect_log')
    op.drop_index(op.f('ix_redirect_log_ip'), table_name='redirect_log')
    op.drop_index(op.f('ix_redirect_log_code'), table_name='redirect_log')
    op.drop_table('redirect_log')
    op.drop_index(op.f('ix_redirect_list_url'), table_name='redirect_list')
    op.drop_index(op.f('ix_redirect_list_description'), table_name='redirect_list')
    op.drop_index(op.f('ix_redirect_list_code'), table_name='redirect_list')
    op.drop_table('redirect_list')
    # ### end Alembic commands ###
