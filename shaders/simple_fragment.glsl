#version 330

in vec2 f_tex_coord;
uniform sampler2D tex;


void main() {
    vec4 c = texture(tex, f_tex_coord);
//    c.a = 0.5;
    gl_FragColor = c;
//    gl_FragColor = vec4(f_tex_coord, co.x, 1.);
}