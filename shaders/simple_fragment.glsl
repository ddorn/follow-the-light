#version 330

in vec2 f_tex_coord;
in vec4 tex_rect;
uniform sampler2D tex;


void main() {
    vec2 coord = tex_rect.xy + tex_rect.zw * fract(f_tex_coord);
    vec4 c = texture(tex, coord);
//    c.a = 0.5;
    gl_FragColor = c;
//    gl_FragColor = vec4(f_tex_coord, co.x, 1.);
}