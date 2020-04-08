#version 330

in vec3 vert;
in vec2 tex_coord;

// xy is center of camera and zw is the size of the view
uniform vec4 camera;

out vec2 f_tex_coord;
out vec3 f_pos;

void main() {
    f_tex_coord = tex_coord;
    vec2 xy = (vert.xy - camera.xy) / camera.zw * 2.0;
    gl_Position = vec4(xy, vert.z, 1.0);
    f_pos = vec3(xy, vert.z);
}
