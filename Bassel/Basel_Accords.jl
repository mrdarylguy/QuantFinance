using JuMP, Cbc, Plots
plotly()
Plots.PlotlyBackend()

m=Model(Cbc.Optimizer)

@variable(m, 0 <= L <= 1)
@variable(m, 0 <= D <= 1)

r_1 = 0.3
r_2 = 0.1
r_3 = 0.25
r_4 = 0.7
α = 0.3

m_d = 0.02
m_l = 0.03

#Declare objective function
@objective(m, Max, m_d*D + m_l*L)

#Declare constraints
@constraint(m, constraint1, D + r_1*L <= 1)
@constraint(m, constraint2, D <= 1 - r_2)
@constraint(m, constraint3, r_3*D + L <= 1)
@constraint(m, constraint4, r_4*L + (1-α)*D <= 1)

#plot graph of state space
line_1(x) = (1-x)/r_1
line_3(x) = 1 - r_3*x
line_4(x) = (1+(α-1)*x)/r_4

plot1 = plot([line_1, line_3, line_4], 
              0, 1,
              ylim=(0, 1.2), 
              xlim=(0, 1.2), 
              label="Deposits", 
              ylabel="Loans")
      
plot1 = plot!([1-r_2], seriestype="vline")
plot1 = annotate!(1-r_2, 0, text("$(1-r_2)"))

savefig(plot1, "state_space.png")

optimize!(m)

println(getvalue(L))
println(getvalue(D))

println("optimal solution occurs at: ", round(objective_value(m), digits=5), "\n")
println("Loans: ", round(getvalue(L)*100, sigdigits=3), "%")
println("liquidity reserves: ", round((100 - getvalue(L)*100), sigdigits=3), "%")
println("\n")
println("Deposits: ", round(getvalue(D)*100, sigdigits=3), "%")
println("Capital: ", round((100 - getvalue(D)*100), sigdigits=3), "%")
