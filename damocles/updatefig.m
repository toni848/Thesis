fig=gcf;
set(findall(fig,'-property','FontSize'),'FontSize',18)
axesObj=fig.Children
%set(axesObj(2),'FontSize',14)
%set(axesObj(1),'FontSize',14)
str=get(fig,'FileName');
savefig(str)
str2=str(1:end-4);
saveas(gcf,[str2,'.eps'],'epsc')