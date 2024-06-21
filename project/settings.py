import flask, flask_sqlalchemy, flask_migrate


project_log = flask.Flask(
    import_name = "project",
    template_folder = "templates"
)

project_log.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = flask_sqlalchemy.SQLAlchemy(app = project_log)

migrate = flask_migrate.Migrate(app = project_log, db = db)