"""Participant ticket number removed

Revision ID: 2514e39b5eaa
Revises: 2a3f8c4f02a2
Create Date: 2013-07-10 18:30:45.815211

"""

# revision identifiers, used by Alembic.
revision = '2514e39b5eaa'
down_revision = '2a3f8c4f02a2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('participant', u'ticket_number')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('participant', sa.Column(u'ticket_number', sa.INTEGER(), nullable=True))
    ### end Alembic commands ###
