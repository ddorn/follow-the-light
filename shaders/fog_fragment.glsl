#version 330

in vec2 f_pos;
uniform float u_time;
uniform vec4 camera;


// Author @patriciogv - 2015
// http://patriciogonzalezvivo.com

#ifdef GL_ES
precision mediump float;
#endif


float random (in vec2 _st) {
    return fract(sin(dot(_st.xy,
                         vec2(12.9898,78.233)))*
        43758.5453123);
}


float noise(vec2 st) {
    st.y += st.x * 0.5;
    st.x /= 0.86;
    vec2 i = floor(st);
    vec2 f = fract(st);

    // Four corners in 2D of a tile
    float a = random(i);
    float b = (f.y >= f.x)
        ? random(i + vec2(0.0, 1.0))
        : random(i + vec2(1.0, 0.0));
    float c = random(i + vec2(1.0, 1.0));

    if (f.y >= f.x) {
        f = f.yx;
    }

    // Barycentric coordinates according to
    // https://en.wikipedia.org/wiki/Barycentric_coordinate_system#Conversion_between_barycentric_and_Cartesian_coordinates
    vec3 l = vec3(1. - f.x, f.x - f.y, f.y);

    return dot(l, vec3(a, b, c));
}


#define NUM_OCTAVES 6

//float fbm ( in vec2 _st) {
//    float v = 0.0;
//    float a = 0.5;
//    vec2 shift = vec2(100.0);
//    // Rotate to reduce axial bias
//    mat2 rot = mat2(cos(0.5), sin(0.5),
//                    -sin(0.5), cos(0.50));
//    for (int i = 0; i < NUM_OCTAVES; ++i) {
//        v += a * noise(_st);
//        _st = rot * _st * 2.0 + shift;
//        a *= 0.5;
//    }
//    return v;
//}

//vec3 damn() {
//    vec2 st = f_pos.xy*3.;
//    // st += st * abs(sin(u_time*0.1)*3.0);
//    vec3 color = vec3(0.0);
//
//    vec2 q = vec2(0.);
//    q.x = fbm( st + 0.00*u_time);
//    q.y = fbm( st + vec2(1.0));
//
//    vec2 r = vec2(0.);
//    r.x = fbm( st + 1.0*q + vec2(1.7,9.2)+ 0.15*u_time );
//    r.y = fbm( st + 1.0*q + vec2(8.3,2.8)+ 0.126*u_time);
//
//    float f = fbm(st+r);
//
//    color = mix(vec3(0.101961,0.619608,0.666667),
//                vec3(0.666667,0.666667,0.498039),
//                clamp((f*f)*4.0,0.0,1.0));
//
//    color = mix(color,
//                vec3(0,0,0.164706),
//                clamp(length(q),0.0,1.0));
//
//    color = mix(color,
//                vec3(0.666667,0.8,0.8),
//                clamp(length(r.x),0.0,1.0));
//
//    return (f*f*f+.6*f*f+.5*f)*color;
//}

void main() {
    vec2 pos = f_pos * camera.zw / camera.z;
//    vec3 fog = smoothstep(-0.99, 1.0, damn());
    float fog = noise(pos * 15.);
//    fog *= vec3(0.5, 0.8, 0.7);
//    float a = length(fog) * 0.5 + 0.2;
//    a = smoothstep(0.0, 1.0, a);
    gl_FragColor = vec4(fog);
}
