// g++ canvas-gen.cpp

#include <iostream>
#include <string>

// dimensions of the output matrix
#define CANVAS_HEIGHT 37
#define CANVAS_WIDTH 50

int main()
{

    // Prints to standard output
    //
    // I use following command to copy
    // the output to clipboard.
    // ./a.out | xclip -sel clip

    std::cout << "<g id=\"outerBox\" data-hydro-click=\"{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:48585950,&quot;target&quot;:&quot;CONTRIBUTION_CALENDAR_SQUARE&quot;,&quot;user_id&quot;:48585950,&quot;originating_url&quot;:&quot;#&quot;}}\"data-hydro-click-hmac=\"5cac6cd55d3bddea9c9341bbf2e39051353c3978362fa7ae27a08becc565e021\"transform=\"translate(10, 20)\">\n";

    for (int x_cord = 0; x_cord < CANVAS_WIDTH; ++x_cord)
    {
        std::cout << "<g transform=\"translate(" << x_cord * 14 << ", 0)\">\n";
        for (int y_cord = 0; y_cord < CANVAS_HEIGHT; ++y_cord)
        {
            std::cout << "<rect width=\"10\" height=\"10\" x=\"" << 14 - x_cord << "\" y=\"" << y_cord * 13 << "\" class=\"ContributionCalendar-day\" rx=\"2\" ry=\"2\" data-count=\"0\" data-date=\"2020-06-07\" data-level=\"4\"></rect>\n";
        }
        std::cout << "</g>\n";
    }
    std::cout << "</g>\n";
    return 0;
}
