#!/usr/bin/python

"""
    The run module starts the application
"""

from server import app, create_app


if __name__ == '__main__':
    create_app()
    app.run(debug=True, host='0.0.0.0', port='8000')
