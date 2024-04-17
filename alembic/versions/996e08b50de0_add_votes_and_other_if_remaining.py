"""add votes and other if remaining

Revision ID: 996e08b50de0
Revises: 893d3c09db4b
Create Date: 2024-04-17 16:27:36.979543

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "996e08b50de0"
down_revision = "893d3c09db4b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "votes",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["post_id"], ["posts.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id", "post_id"),
    )
    op.drop_constraint("posts_users_fk", "posts", type_="foreignkey")
    op.create_foreign_key(
        None, "posts", "users", ["owner_id"], ["id"], ondelete="CASCADE"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "posts", type_="foreignkey")
    op.create_foreign_key(
        "posts_users_fk",
        "posts",
        "users",
        ["owner_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_table("votes")
    # ### end Alembic commands ###
