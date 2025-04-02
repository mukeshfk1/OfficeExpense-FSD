from flask import render_template, request, redirect
from app import app
from database import db, Expense


@app.route('/')
def home():
    try:
    
        expenses = Expense.query.order_by(Expense.id.desc()).all()
        return render_template('index.html', expenses_data=expenses)
    
    except Exception as e:
        return {"error": str(e)}
    

@app.route('/new-transaction', methods=['GET', 'POST'])
def new_transaction():
    try:
        if request.method == "POST":
            
            ammount = request.form.get('amount')
            description = request.form.get('description')
            transaction_type = request.form.get('transaction_type')
        
            last_transaction = Expense.query.order_by(Expense.id.desc()).first()
            previous_balance = last_transaction.running_balance if last_transaction else 0.0
            
            curr_balance = previous_balance + float(ammount) if transaction_type == 'credit' else previous_balance - float(ammount)
    
            new_transaction = Expense(
                description=description,
                transaction_type=transaction_type,
                amount=ammount,
                running_balance=curr_balance
                )
            
            db.session.add(new_transaction)
            db.session.commit()

            return redirect('/')
        
        return render_template('transaction.html')
    
    except Exception as e:
        return {"error": str(e)}


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
