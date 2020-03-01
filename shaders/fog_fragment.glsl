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

vec3 noise(vec2 st) {

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
    return vec3(.5*r + 0.5) ;
}


void main() {
    vec2 pos = f_pos * camera.zw / camera.z;
    pos += mod(u_time, 10000.) * vec2(1., 0.2) * 0.1;


    vec3 color = noise(pos * 13.);

    vec3 c1 = vec3(1.0, 0.647, 0.0);
    vec3 c2 = vec3(0.204, 0.725, 0.627);
    vec3 c3 = vec3(0.78, 0.922, 0.463);

//    fog *= vec3(0.5, 0.8, 0.7);
//    float a = length(fog) * 0.5 + 0.2;
//    a = smoothstep(0.0, 1.0, a);
    gl_FragColor = vec4(color, 1.);
}
