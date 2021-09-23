using Polynomials
using Roots

market_price = 91.0
par_value = 100.0
coupon = 6.0
y_t_r = 3

f(k) = coupon/(1+k) + coupon/(1+k)^2 + coupon/(1+k)^3 + par_vale(1+k)^y_t_r - market_price

# z = 1(1+k)
# k = 1/z - 1


f(z) = (par_value + coupon)*z^3 + coupon*z^2 + coupon^z - market_price

sol = find_zero(f, (0,1)) 
k = (1/sol - 1) * 100