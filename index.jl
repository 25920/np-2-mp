m_complex = [
    1 2im -1im 4-1im;
    -2im 8 6im 8+1im;
    1im -6im 12 1im;
    4+1im 8-1im -1im 20
] # complex matrix

m_conjugate = conj(m_complex) # conjugated form

m_transpose = transpose(m_conjugate) # conjugate transpose

m_c_m_ct = false

if m_transpose==m_complex
    m_c_m_ct=true
end

# println("complex matrix M\n$m_complex")

# println("its conjugation\n$m_conjugate")

# println("and its hermitian transpose\n$m_transpose")

println("as m == m's conjugate transpose => $(m_c_m_ct)")

if m_c_m_ct==true
    println("m is a hermitian matrix")
end
