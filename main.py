from app import create_app

# __name__ CHANGES TO __main__ WHENEVER THE FILE IS RUNNING
if __name__ == "__main__":
  app = create_app()
  app.run(debug=True, port = 3000) # FOR DEVELOPMENT PURPOSE      