#version 330

in vec2 f_pos;
uniform float u_time;
uniform vec4 camera;


#ifdef GL_ES
precision mediump float;
#endif


/// Return a determistic random value between 0 and 1.
/// This function was taken from The Book of Shaders.
float random (in vec2 _st) {
    return fract(sin(dot(_st.xy,
                         vec2(12.9898,78.233)))*
        43758.5453123);
}


/// Return a vec2 in the unit sphere
vec2 random2(vec2 st){
    float a = random(st) * 6.1831;
    return vec2(cos(a), sin(a));
}


vec2 skew (vec2 st) {
    vec2 r = vec2(0.0);
    r.x = 1.1547*st.x;
    r.y = st.y+0.5*r.x;
    return r;
}


/// Return a random value in [0,1]. This function is continuous.
float noise(vec2 st) {

    st = skew(st);
    vec2 i = floor(st);
    vec2 f = fract(st);
    vec2 u = f*f*f*(f*(f*6.-15)+10);

    // A random gradient for each corner of the simplex
    vec2 op = (f.y >= f.x) ? vec2(0.0, 1.0) : vec2(1.0, 0.0);
    vec2 a = random2(i);
    vec2 b = random2(i + op);
    vec2 c = random2(i + vec2(1.0, 1.0));

    // Dot pruduct between the random gradient and
    // the vecteur comming from the corner
    vec3 t = vec3(
        dot(a, (f)),
        dot(b, (f - op)),
        dot(c, (f - 1.))
    );

    if (u.y >= u.x) {
        u = u.yx;
    }

    // Barycentric coordinates according to
    // https://en.wikipedia.org/wiki/Barycentric_coordinate_system#Conversion_between_barycentric_and_Cartesian_coordinates
    vec3 l = vec3(1. - u.x, u.x - u.y, u.y);
    float r = dot(t, l);
    return .5*r + 0.5;
}

vec3 fog(vec2 st) {

    vec3[5] colors = vec3[5](
        vec3(0.22, 0.486, 0.302),
        vec3(0.776, 0.792, 0.439),
        vec3(0.443, 0.161, 0.255),
        vec3(0.),
        vec3(0.)
    );

    float amp = 1.;
    float freq = 1.;

    float gain = 0.4;
    float lacunarity = 2.3;

    int octaves = 3;
    float f = 0;
    for (int i = 0; i < octaves; ++i) {
        f += noise(st * freq + u_time /4.) * amp;
        amp *= gain;
        freq *= lacunarity;
    }

    float amp_tot = (1. - pow(gain, octaves + 1.)) / (1. - gain);

    return vec3(f / amp_tot);
}

void main() {
    vec2 pos = f_pos * camera.zw / camera.z;
    pos *= 8;
    pos += vec2(-.5, 1.) * u_time / 3;
    vec3 color = (fog(pos * 5.)) * 3.* vec3(0.076, 0.218, 0.324);

    float c1 = 10;
    float c2 = 5;
    vec2 d1 = vec2(1) * u_time / 2. ;
    float d2 = u_time / 10.;

    float f = noise(pos.yx + d1 + c1 * noise(pos + d2 + c2 * noise(pos)));

    vec3 a = vec3(0.0);
    vec3 b = vec3(0.3, 0.1, 0.2);
    vec3 c = vec3(0.22, 0.741, 0.616);
    vec3 d = vec3(0.965, 0.971, 0.349);

    vec3 p = vec3(0.4, 0.6, 0.7);

    if (f < p.x) {
        color = mix(a, b, f);
    } else if (f < p.y) {
        color = mix(b, c, smoothstep(p.x, p.y, f));
    } else {
        color = mix(c, d, smoothstep(p.y, p.z, f));
    }

    gl_FragColor = vec4(color, 1.) ;
}
