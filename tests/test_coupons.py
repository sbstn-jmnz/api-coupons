from app.coupons import apply_coupon, get_final_price

def test_sales10():
  assert apply_coupon(100, "SALES10") == 90.0

def test_super20():
  assert apply_coupon(200, "SUPER20") == 160.0

def test_welcome():
  assert apply_coupon(100, "WELCOME") == 85.0

def test_invalid_coupon():
  assert apply_coupon(990,"FAKE") == 990

def test_final_price_with_tax():
  assert get_final_price(100, "SALES10") == 107.1