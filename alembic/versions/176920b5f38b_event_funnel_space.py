"""Event.funnel_space

Revision ID: 176920b5f38b
Revises: 5a2784d6249f
Create Date: 2014-02-09 02:23:59.109416

"""

# revision identifiers, used by Alembic.
revision = '176920b5f38b'
down_revision = '5a2784d6249f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('funnel_space', sa.Unicode(length=25), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'funnel_space')
    ### end Alembic commands ###
