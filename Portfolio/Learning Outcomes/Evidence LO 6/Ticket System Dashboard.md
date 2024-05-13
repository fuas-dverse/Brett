# [[Ticket System Dashboard]]
# Table of Contents
- [Context](#Context)
- [Security Measures](#Security%20Measures)
	- [Authorization](#Authorization)
		- [Middleware](#Middleware)
	- [Security Headers](#Security%20Headers)
		- [Security Headers Implementation](#Security%20Headers%20Implementation)
			- [X-Frame-Options](#X-Frame-Options)
			- [Permissions-Policy](#Permissions-Policy)
			- [Strict-Transport-Security (HSTS)](#Strict-Transport-Security%20(HSTS))
			- [X-Content-Type-Options](#X-Content-Type-Options)
			- [Referrer-Policy](#Referrer-Policy)
			- [X-XSS-Protection](#X-XSS-Protection)
	- [Supabase Row Level Security](#Supabase%20Row%20Level%20Security)
		- [My rules for the application](#My%20rules%20for%20the%20application)

## Context
The Ticket System Dashboard is designed to securely manage API access for Ticket System Agents, enabling targeted functionality based on user roles and permissions. This dashboard allows users to request keys for API access, ensuring secure interactions within the system. The dashboard’s backend leverages the robust capabilities of NextJS 14 and Supabase Auth to facilitate these operations.

## Security Measures

### Authorization
The Ticket System Dashboard is designed to securely manage API access for Ticket System Agents, enabling targeted functionality based on user roles and permissions. This dashboard allows users to request keys for API access, ensuring secure interactions within the system. The dashboard’s backend leverages the robust capabilities of NextJS 14 and Supabase Auth to facilitate these operations.
#### Middleware
In the provided code snippet, the middleware function `updateSession` plays a crucial role in managing session states across client-server interactions. This function utilizes the `createServerClient` from the Supabase SSR package to handle the delicate task of managing cookie data securely and efficiently.

```ts
import { createServerClient, type CookieOptions } from "@supabase/ssr";  
import { type NextRequest, NextResponse } from "next/server";  
  
export const updateSession = async (request: NextRequest) => {  
    // This `try/catch` block is only here for the interactive tutorial.  
    // Feel free to remove once you have Supabase connected.    try {  
        // Create an unmodified response  
        let response = NextResponse.next({  
            request: {  
                headers: request.headers,  
            },  
        });  
  
        const supabase = createServerClient(  
            process.env.NEXT_PUBLIC_SUPABASE_URL!,  
            process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,  
            {  
                cookies: {  
                    get(name: string) {  
                        return request.cookies.get(name)?.value;  
                    },  
                    set(name: string, value: string, options: CookieOptions) {  
                        // If the cookie is updated, update the cookies for the request and response  
                        request.cookies.set({  
                            name,  
                            value,  
                            ...options,  
                        });  
                        response = NextResponse.next({  
                            request: {  
                                headers: request.headers,  
                            },  
                        });  
                        response.cookies.set({  
                            name,  
                            value,  
                            ...options,  
                        });  
                    },  
                    remove(name: string, options: CookieOptions) {  
                        // If the cookie is removed, update the cookies for the request and response  
                        request.cookies.set({  
                            name,  
                            value: "",  
                            ...options,  
                        });  
                        response = NextResponse.next({  
                            request: {  
                                headers: request.headers,  
                            },  
                        });  
                        response.cookies.set({  
                            name,  
                            value: "",  
                            ...options,  
                        });  
                    },  
                },  
            },  
        );  
  
        // This will refresh session if expired - required for Server Components  
        // https://supabase.com/docs/guides/auth/server-side/nextjs        await supabase.auth.getUser();  
  
        return response;  
    } catch (e) {  
        // If you are here, a Supabase client could not be created!  
        // This is likely because you have not set up environment variables.        // Check out http://localhost:3000 for Next Steps.        return NextResponse.next({  
            request: {  
                headers: request.headers,  
            },  
        });  
    }  
};
```

The middleware operates by setting up a client with environment-specific credentials and cookie management options. Here’s how it handles cookies:

- **Getting Cookies**: The middleware retrieves cookie values from incoming requests. This is crucial for maintaining session continuity, allowing the server to recognize returning users and adjust responses based on their authenticated state.
    
- **Setting Cookies**: Whenever user authentication states change, such as during login or when refreshing tokens, the middleware updates the cookie in both the request and the response objects. This ensures that the client-side application remains synchronized with the server-side authentication state.
    
- **Removing Cookies**: If a user logs out or if a session becomes invalid, the middleware removes the corresponding cookies. This step is vital for preventing stale or potentially insecure session data from persisting on the client side.

These operations ensure that the authentication flow is seamless and secure, leveraging HTTP-only cookies to safeguard against client-side script access to sensitive information. By managing cookies at the middleware level, the application enhances security by isolating authentication logic from the business logic layers, reducing the risk of unauthorized access and CSRF attacks.

This middleware integration with Supabase auth and Next.js provides a robust framework for handling user sessions and authentication states, which is essential for maintaining a secure and user-friendly web application environment.

### Security Headers
Upon successful authentication, users are granted access based on predefined roles that determine the level of API interaction permissible. This role-based access control is essential for maintaining the integrity and confidentiality of the system. It ensures that users can only access resources appropriate to their role, preventing unauthorized data access and modification.

#### Security Headers Implementation
Security headers play a pivotal role in protecting the application from various types of attacks. Below is a breakdown of the security headers configured in the NextJS application:

##### X-Frame-Options
Set to `DENY`, this header prevents the application from being displayed in an `<iframe>`, safeguarding against clickjacking attacks.

##### Permissions-Policy
This header controls which features the application can request permission to use, specifying that most features are disabled (`accelerometer`, `camera`, etc.) except where explicitly allowed. This minimizes the risk of invasive features being exploited maliciously.

##### Strict-Transport-Security (HSTS)
The inclusion of `max-age=63072000; includeSubDomains; preload` enforces the strict use of HTTPS across all subdomains for two years, including preloading into browsers. This prevents SSL stripping attacks and ensures secure connections.

##### X-Content-Type-Options
Set to `nosniff`, this header prevents the browser from trying to MIME-sniff the content type, which can lead to security vulnerabilities.

##### Referrer-Policy
Configured to `origin-when-cross-origin`, this setting controls the amount of referrer information sent with requests, protecting user privacy and reducing the risk of referrer leakage.

##### X-XSS-Protection
Enabled with `1; mode=block`, this header activates built-in browser filters to prevent cross-site scripting (XSS) attacks, where older browsers do not support newer standards like Content Security Policy (CSP).

All of these headers have been set in the `next.config.mjs`
```js
/** @type {import('next').NextConfig} */  
const nextConfig = {  
    // ... Aditional options
    async headers() {  
        return [  
            {  
                source: '/(.*)', // Use '*' for all routes  
                headers: [  
                    {  
                        key: 'X-Frame-Options',  
                        value: 'DENY',  
                    },  
                    {  
                        key: 'Permissions-Policy',  
                        value: 'accelerometer=(), ambient-light-sensor=(), autoplay=(), battery=(), camera=(), cross-origin-isolated=(self), display-capture=(), document-domain=(), encrypted-media=(), execution-while-not-rendered=(), execution-while-out-of-viewport=(), fullscreen=(self), geolocation=(), gyroscope=(), keyboard-map=(), magnetometer=(), microphone=(self), midi=(), navigation-override=(), payment=(), picture-in-picture=(), publickey-credentials-get=(), screen-wake-lock=(), sync-xhr=(), usb=(), web-share=(), xr-spatial-tracking=()',  
                    },  
                    {  
                        key: 'Strict-Transport-Security',  
                        value: 'max-age=63072000; includeSubDomains; preload'  
                    },  
                    {  
                        key: 'X-Content-Type-Options',  
                        value: 'nosniff'  
                    },  
                    {  
                        key: 'Referrer-Policy',  
                        value: 'origin-when-cross-origin'  
                    },  
                ],  
            },  
            {  
                source: '/((?!api|_next/static|_next/image|favicon.ico|mastodon-icon.svg).*)',  
                headers: [  
                    {  
                        key: 'X-XSS-Protection',  
                        value: '1; mode=block'  
                    },  
                ],  
            },  
        ];  
    },  
};  
  
export default nextConfig;
```

### Supabase Row Level Security
In order to keep the data save and only available in the Dashboard Application (for now, because the keys needs to be accessed later in the API's). I added Row Level Security rules. Those rules tells the Supabase that tables in the database can be accessed if it requires the assigned rule. For example: Enable read access for all users that are authenticated for the `available_keys` table.

With this rule, all authenticated users can read data from the `available_keys` table. This means that in no case they can change the database or add a new row their selfs.

#### My rules for the application
![[Screenshot 2024-05-13 at 10.50.56.png]]


