"""AI-generated learning example. Demonstration parameters, not measured data.
Run with Python 3; standard library only. Analytical branch: underdamped only.
"""
from pathlib import Path
import math
import csv
import json
import html

M, C, K, F0, OMEGA = 1.0, 0.8, 4.0, 1.0, 1.5
X0, V0, T, H = 0.0, 0.0, 30.0, 0.01
OUT = Path(__file__).resolve().parent / 'simulation'

def exact(t, c=C):
    if not (M > 0 and K > 0 and 0 < c < 2*math.sqrt(M*K)):
        raise ValueError('Analytical branch requires m,k>0 and 0<c<2 sqrt(mk)')
    alpha = c/(2*M)
    wd = math.sqrt(K/M-alpha*alpha)
    d = K-M*OMEGA**2
    q = d*d+(c*OMEGA)**2
    a, b = F0*d/q, F0*c*OMEGA/q
    cc = X0-a
    ee = (V0-b*OMEGA+alpha*cc)/wd
    ss = a*math.cos(OMEGA*t)+b*math.sin(OMEGA*t)
    sv = -a*OMEGA*math.sin(OMEGA*t)+b*OMEGA*math.cos(OMEGA*t)
    sa = -OMEGA**2*ss
    g = cc*math.cos(wd*t)+ee*math.sin(wd*t)
    gp = wd*(-cc*math.sin(wd*t)+ee*math.cos(wd*t))
    exp = math.exp(-alpha*t)
    return (ss+exp*g, sv+exp*(gp-alpha*g),
            sa+exp*((alpha**2-wd**2)*g-2*alpha*gp), ss)

def integrate(h, c=C):
    n = round(T/h)
    if abs(n*h-T)>1e-10:
        raise ValueError('T must be divisible by h')
    def f(t, x, v):
        return v, (F0*math.cos(OMEGA*t)-c*v-K*x)/M
    x, v = X0, V0
    rows = []
    for i in range(n+1):
        t = i*h
        xa, va, acc, ss = exact(t, c)
        rows.append((t, x, v, xa, ss, x-xa))
        if i == n:
            break
        p = f(t,x,v)
        q = f(t+h/2,x+h*p[0]/2,v+h*p[1]/2)
        r = f(t+h/2,x+h*q[0]/2,v+h*q[1]/2)
        s = f(t+h,x+h*r[0],v+h*r[1])
        x += h*(p[0]+2*q[0]+2*r[0]+s[0])/6
        v += h*(p[1]+2*q[1]+2*r[1]+s[1])/6
    return rows

def panel(series, ytop, title, ylabel, xmin=0, xmax=T):
    # series: label, color, dash, list of (time, value)
    left, width, height = 90, 810, 215
    ys = [y for _,_,_,pts in series for x,y in pts if xmin<=x<=xmax]
    lo, hi = min(ys), max(ys)
    pad = (hi-lo)*0.12 or 1
    lo, hi = lo-pad, hi+pad
    def point(x,y):
        return left+(x-xmin)*width/(xmax-xmin), ytop+height-(y-lo)*height/(hi-lo)
    out = [f'<text x="90" y="{ytop-18}" font-size="18">{html.escape(title)}</text>']
    for i in range(6):
        x=xmin+(xmax-xmin)*i/5
        px,_=point(x,lo)
        out += [f'<path d="M{px},{ytop} v{height}" stroke="#e2e8f0"/>',f'<text x="{px}" y="{ytop+height+22}" text-anchor="middle">{x:g}</text>']
        y=lo+(hi-lo)*i/5
        _,py=point(xmin,y)
        out += [f'<path d="M{left},{py} h{width}" stroke="#e2e8f0"/>',f'<text x="80" y="{py+4}" text-anchor="end">{y:.3g}</text>']
    out += [f'<rect x="{left}" y="{ytop}" width="{width}" height="{height}" fill="none" stroke="#64748b"/>',f'<text x="495" y="{ytop+height+47}" text-anchor="middle">Time (s)</text>',f'<text transform="translate(23,{ytop+height/2}) rotate(-90)" text-anchor="middle">{ylabel}</text>']
    for j,(label,color,dash,pts) in enumerate(series):
        pts=[p for p in pts if xmin<=p[0]<=xmax]
        coords=' '.join(f'{px:.2f},{py:.2f}' for px,py in (point(x,y) for x,y in pts))
        out += [f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="2" stroke-dasharray="{dash}"/>']
        xx=95+j*265
        out += [f'<path d="M{xx},{ytop+height+74} h25" stroke="{color}" stroke-width="3" stroke-dasharray="{dash}"/>',f'<text x="{xx+32}" y="{ytop+height+79}">{html.escape(label)}</text>']
    return ''.join(out)

def svg(name, title, content):
    text=f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="890" viewBox="0 0 960 890"><rect width="960" height="890" fill="white"/><g font-family="Arial, sans-serif" font-size="13" fill="#172033"><text x="90" y="34" font-size="23">{title}</text><text x="90" y="61">ILLUSTRATIVE VALUES | m=1 kg, k=4 N/m, F0=1 N, omega=1.5 rad/s, x0=v0=0</text>{content}<text x="90" y="870">Learning example: mathematical consistency checks, no experimental validation.</text></g></svg>'
    (OUT/name).write_text(text,encoding='utf-8')

def main():
    OUT.mkdir(exist_ok=True)
    rows=integrate(H)
    fine=integrate(H/2)
    err=max(abs(r[5]) for r in rows)
    fine_err=max(abs(r[5]) for r in fine)
    residual=max(abs(M*exact(r[0])[2]+C*exact(r[0])[1]+K*exact(r[0])[0]-F0*math.cos(OMEGA*r[0])) for r in rows)
    assert err < 1e-6 and fine_err < err, 'Accuracy or refinement check failed'
    assert abs(exact(0)[0]-X0)<1e-12 and abs(exact(0)[1]-V0)<1e-12
    assert residual < 1e-12
    def save(name, rr):
        with (OUT/name).open('w',newline='',encoding='utf-8') as f:
            w=csv.writer(f)
            w.writerow(['time_s','rk4_x_m','rk4_v_m_per_s','analytical_x_m','steady_x_m','signed_error_m'])
            w.writerows(rr)
    save('baseline.csv',rows)
    traces=[]
    amplitudes={}
    for c,color in [(0.4,'#1d4ed8'),(0.8,'#b45309'),(1.6,'#0f766e')]:
        rr=integrate(H,c)
        assert max(abs(r[5]) for r in rr)<1e-6
        save(f'damping_{c:g}.csv',rr)
        traces.append((f'c={c:g} N s/m',color,'',[(r[0],r[1]) for r in rr]))
        amplitudes[str(c)]=F0/math.sqrt((K-M*OMEGA**2)**2+(c*OMEGA)**2)
    svg('figure1.svg','Figure 1 Analytical and numerical response',
        panel([('Analytical','#1d4ed8','',[(r[0],r[3]) for r in rows]),('RK4 h=0.01 s','#b45309','7 5',[(r[0],r[1]) for r in rows]),('Steady periodic','#0f766e','3 4',[(r[0],r[4]) for r in rows])],115,'Baseline c=0.8 N s/m','Displacement (m)')+
        panel([('RK4 minus analytical','#b45309','',[(r[0],r[5]) for r in rows])],505,'Numerical error','Error (m)'))
    svg('figure2.svg','Figure 2 Effect of damping',panel(traces,115,'Early response','Displacement (m)',0,12)+panel(traces,505,'Late response','Displacement (m)',20,30))
    metrics={'parameters':{'m_kg':M,'c_Ns_per_m':C,'k_N_per_m':K,'F0_N':F0,'omega_rad_per_s':OMEGA,'x0_m':X0,'v0_m_per_s':V0,'T_s':T},'parameter_source':'self-selected illustrative values, not literature or experimental values','method':'fixed-step classical RK4','h_s':H,'max_abs_error_m':err,'half_step_max_abs_error_m':fine_err,'error_ratio':err/fine_err,'analytical_ode_residual_max_N':residual,'analytical_initial_x_m':exact(0)[0],'analytical_initial_v_m_per_s':exact(0)[1],'steady_amplitudes_m':amplitudes,'python_version':__import__('sys').version}
    (OUT/'metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
    print(json.dumps(metrics,indent=2))

if __name__=='__main__':
    main()
