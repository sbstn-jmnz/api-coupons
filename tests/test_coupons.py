from app.coupons import apply_coupon, get_final_price

def test_descuento_oferta10():
  assert apply_coupon(100, "SALES10") == 90.0

def test_descuento_super20():
  assert apply_coupon(200, "SUPER20") == 160.0

def test_descuento_bienvenida():
  assert apply_coupon(100, "WELCOME") == 85.0

def test_precio_final_con_impuesto():
  assert get_final_price(100, "SALES10") == 107.1