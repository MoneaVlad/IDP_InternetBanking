from internet_banking import app, metrics

if __name__ == '__main__':
    metrics.init_app(app)
    app.run(host= '0.0.0.0', port=5000, debug=True)
