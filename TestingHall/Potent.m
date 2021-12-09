clear all; clc;
%% CALCULATEUR D'ECOULEMENT POTENTIEL
% Ce programme à pour but de modéliser un ensemble quelconque d'écoulement
% potentiel dans un domaine donné

% Probleme theta tend vers infini quand x-x0 tend vers 0
%% Parametres

% Domaine
X_limit = [-2 2];
Y_limit = [-2 2];
Nx = 300; Ny = 300;
epsilon = 0.001;
[x,y] = meshgrid(...
    [linspace(X_limit(1),-epsilon,Nx/2) linspace(-epsilon,epsilon,20*Nx)...
    linspace(epsilon,X_limit(2),Nx/2)],...
    linspace(Y_limit(1),Y_limit(2),Ny));
    

    %[linspace(Y_limit(1),-epsilon,Ny/2) linspace(-epsilon,epsilon,20*Ny)...
    %linspace(epsilon,Y_limit(2),Ny/2)]);

%[x,y] = meshgrid( linspace(X_limit(1),X_limit(2),Nx) ,...
%                  linspace(Y_limit(1),Y_limit(2),Ny));


%% Ecoulement Potentiel
[phi(:,:,1),psi(:,:,1)] = Potent_Uniforme(1,1,0,x,y);

%[phi(:,:,3),psi(:,:,3)] = Potent_Source(1,0,0,x,y);
%[phi(:,:,4),psi(:,:,4)] = Potent_Source(1,0,1,x,y);
%[phi(:,:,5),psi(:,:,5)] = Potent_Source(1,0,-1,x,y);
[phi(:,:,2),psi(:,:,2)] = Potent_Source(-200,0.01,0,x,y);
[phi(:,:,3),psi(:,:,3)] = Potent_Source(200,-0.01,0,x,y);

%[phi(:,:,5),psi(:,:,5)] = Potent_Source(-1,5.1,0,x,y);
[phi(:,:,4),psi(:,:,4)] = Potent_Tourbillon(-10,0,0,x,y);

%% COURBES
t_1 = [0:1:5];
x_1 = t_1;
y_1 = t_1;
%for i=1:length(t_1)
%    [phi(:,:,10+i),psi(:,:,10+i)] = Potent_Source(1,x_1(i),y_1(i),x,y);
%end


%% Sommes des potentiels
PHI = sum(phi,3);
PSI = sum(psi,3);

%% Visualisation
figure(1); clf;
contour(x,y,PHI,30,'LineColor',[0.8 0.8 1],'LineStyle','--',...
    'ShowText','off'); hold on;
contour(x,y,PSI,[-3:0.5:-0.5 -0.5:0.1:0.5 0.5:0.5:3],'LineColor',...
    [0.3 0.3 1],'LineStyle','-',...
    'ShowText','off'); hold on;
legend('Potentiel','Fct de courant');

cd('/Users/floriandelrieu/OneDrive/Cours/MATLAB/Function_PERSOS');
Ray = [0.6:0.01:0.8];
for int=1:length(Ray)
DrawCircle([0 0],Ray(int))
end
axis equal
%pbaspect([1 1 1]);

%figure(2);clf;
%[r,theta] = cylind(0,0,x,y);
%contour(x,y,theta,30,'ShowText','on'); hold on
%contour(x,y,asin((y-y0)./rho),'ShowText','on')
%% Fonction Ecoulement Potentiels

% Ecoulement Uniforme
function [Phi,Psi] = Potent_Uniforme(U,ex,ey,x,y)
    % U: intensité de la vitesse
    % ex,ey: Direction de l'ecoulement
    % x,y: maillage du domaine (coordonées)
    theta = atan(ey/ex);
    Phi = U*cos(theta)*x + U*sin(theta)*y;
    Psi = U*cos(theta)*y - U*sin(theta)*x;
end

% Sources et Puits
function [Phi,Psi] = Potent_Source(Q,x0,y0,x,y)
    % Q: Intensité
    % x0,y0: Position
    % x,y: maillage du domaine (coordonées)
    [r,theta] = cylind(x0,y0,x,y);
    %[r,theta] = cart2pol(x-x0,y-y0);
    Phi = Q/(2*pi).*log(r);
    Psi = Q/(2*pi).*theta;
end

% Tourbillon
function [Phi,Psi] = Potent_Tourbillon(Gamma,x0,y0,x,y)
    % Gamma: Intensité (circulation)
    % x0,y0: Position
    % x,y: maillage du domaine (coordonées)
    [r,theta] = cylind(x0,y0,x,y);
    %[r,theta] = cart2pol(x-x0,y-y0);
    Phi = Gamma/(2*pi).*theta;
    Psi = - Gamma/(2*pi)*log(r);
end

% Calcul des coordonnees cylindirque
function [rho,theta] = cylind(x0,y0,x,y)
    % x0,y0: origine de reference des coordonnees
    % x,y: maillage du domaine
    rho = sqrt((x-x0).^2 + (y-y0).^2);
    theta_x = acos((x-x0)./rho);
    theta_y = asin((y-y0)./rho);
    theta_y(theta_y<0) = -1;
    theta_y(theta_y>=0) = 1;
    theta = theta_y.*theta_x;
end
    
    
    
    
    

